use pyo3::prelude::*;
use pyo3::types::PyDict;

use phenotype_registry::ecosystem::{self, ParseError, RepoEntry};

/// A single repository entry extracted from the ecosystem map.
#[pyclass(from_py_object)]
#[derive(Debug, Clone)]
struct RepoEntryPy {
    /// Repository name (e.g. `"phenotype-registry"`).
    #[pyo3(get)]
    name: String,
    /// Role classification (e.g. `"shared-lib"`, `"SDK"`, `"tooling"`).
    #[pyo3(get)]
    role: String,
    /// Primary programming language, when known.
    #[pyo3(get)]
    language: Option<String>,
    /// Lifecycle status (e.g. `"Active"`, `"Archived"`, `"CANONICAL"`).
    #[pyo3(get)]
    status: Option<String>,
    /// Free-form notes attached to the row.
    #[pyo3(get)]
    notes: Option<String>,
    /// Names of repositories this one depends on.
    #[pyo3(get)]
    dependencies: Vec<String>,
}

#[pymethods]
impl RepoEntryPy {
    /// Return a dictionary representation of the entry.
    fn to_dict(&self, py: Python<'_>) -> PyResult<Py<PyAny>> {
        let dict = PyDict::new(py);
        dict.set_item("name", &self.name)?;
        dict.set_item("role", &self.role)?;
        dict.set_item("language", &self.language)?;
        dict.set_item("status", &self.status)?;
        dict.set_item("notes", &self.notes)?;
        dict.set_item("dependencies", &self.dependencies)?;
        Ok(dict.into_any().unbind())
    }

    fn __repr__(&self) -> String {
        format!(
            "RepoEntryPy(name={:?}, role={:?}, language={:?}, status={:?}, notes={:?}, dependencies={:?})",
            self.name, self.role, self.language, self.status, self.notes, self.dependencies
        )
    }

    fn __str__(&self) -> String {
        format!(
            "RepoEntry({name}, role={role})",
            name = self.name,
            role = self.role
        )
    }
}

impl From<RepoEntry> for RepoEntryPy {
    fn from(entry: RepoEntry) -> Self {
        RepoEntryPy {
            name: entry.name,
            role: entry.role,
            language: entry.language,
            status: entry.status,
            notes: entry.notes,
            dependencies: entry.dependencies,
        }
    }
}

/// Parse an ecosystem map markdown document and return a list of RepoEntryPy objects.
///
/// The function takes a markdown string and parses role classification tables,
/// triage tables, cluster tables, and dependency adjacency lists into a
/// deduplicated list of repository entries.
///
/// Raises:
///     ValueError: If the input is empty or contains malformed tables.
#[pyfunction]
fn parse_ecosystem_map_py(input: &str) -> PyResult<Vec<RepoEntryPy>> {
    match ecosystem::parse_ecosystem_map(input) {
        Ok(entries) => Ok(entries.into_iter().map(RepoEntryPy::from).collect()),
        Err(ParseError::EmptyInput) => {
            Err(pyo3::exceptions::PyValueError::new_err("input is empty"))
        }
        Err(ParseError::MalformedTable { line, detail }) => {
            Err(pyo3::exceptions::PyValueError::new_err(format!(
                "malformed table at line {line}: {detail}"
            )))
        }
    }
}

/// A Python module implemented in Rust for the phenotype-registry Python SDK.
#[pymodule]
fn pheno_registry_python(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    m.add_class::<RepoEntryPy>()?;
    m.add_function(wrap_pyfunction!(parse_ecosystem_map_py, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::collections::HashSet;

    /// A minimal ecosystem map markdown snippet that exercises the parser.
    const ECO_SAMPLE: &str = "\
| Role | Count | Repos |
|------|-------|-------|
| shared-lib | 1 | foo-core |
| SDK | 1 | bar-sdk |

## Dependencies

foo-core -> bar-sdk
";

    #[test]
    fn parse_returns_nonempty_entries() {
        let entries = ecosystem::parse_ecosystem_map(ECO_SAMPLE)
            .expect("parse should succeed on sample input");
        assert!(
            !entries.is_empty(),
            "sample ecosystem map should yield at least one entry"
        );
        let names: HashSet<_> = entries.iter().map(|e| e.name.as_str()).collect();
        assert!(
            names.contains("foo-core"),
            "expected foo-core in parsed entries, got {names:?}"
        );
    }

    #[test]
    fn from_repo_entry_preserves_fields() {
        let entries = ecosystem::parse_ecosystem_map(ECO_SAMPLE).expect("parse should succeed");
        let first = entries.into_iter().next().unwrap();
        let py_entry = RepoEntryPy::from(first.clone());
        assert_eq!(py_entry.name, first.name);
        assert_eq!(py_entry.role, first.role);
        assert_eq!(py_entry.language, first.language);
        assert_eq!(py_entry.status, first.status);
        assert_eq!(py_entry.notes, first.notes);
        assert_eq!(py_entry.dependencies, first.dependencies);
    }

    #[test]
    fn roundtrip_representer_strings() {
        let entry = RepoEntryPy {
            name: "alpha".into(),
            role: "tooling".into(),
            language: Some("Rust".into()),
            status: Some("Active".into()),
            notes: Some("test note".into()),
            dependencies: vec!["beta".into()],
        };
        let repr = entry.__repr__();
        assert!(repr.contains("alpha"), "repr should contain name: {repr}");
        assert!(repr.contains("tooling"), "repr should contain role: {repr}");

        let s = entry.__str__();
        assert!(s.contains("alpha"), "__str__ should contain name: {s}");
        assert!(s.contains("tooling"), "__str__ should contain role: {s}");
    }
}

## Builder Pattern

> **Core idea:** When an object is too complex to create in a single constructor call, use a separate **builder** that constructs it **step-by-step** through a clean API.

---

### 1. Basic Builder (`builder.py`)

**Product** — `HtmlElement` holds the data (`name`, `text`, nested `elements`).  
**Builder** — `HtmlBuilder` owns the root element and exposes methods to add children.

Key takeaways:

* **Simple builder** — call `add_child()` repeatedly, one step at a time.
* **Fluent interface** — `add_child_fluent()` returns `self` so calls can be chained:
  ```python
  builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
  ```
* **Static factory on the product** — `HtmlElement.create('ul')` returns an `HtmlBuilder`. The caller doesn't need to know the builder class exists.

---

### 2. Builder Facets (`builder_facets.py`)

When a single object has **multiple groups of related properties**, split the builder into focused sub-builders (facets).

* `PersonBuilder` is the entry point — it exposes `lives` and `works` properties that return specialized sub-builders.
* `PersonAddressBuilder` handles address fields (`at()`, `in_city()`, `with_postcode()`).
* `PersonJobBuilder` handles job fields (`at()`, `as_a()`, `earning()`).
* Both sub-builders inherit from `PersonBuilder`, so you can **switch between facets mid-chain**:
  ```python
  pb.lives.at("123 London Road").in_city("London").with_postcode("SW12BC") \
    .works.at("Fabrikam").as_a("Engineer").earning(123000) \
    .build()
  ```
* All sub-builders share the **same `Person` instance**, so every facet contributes to one object.

---

### 3. Builder Inheritance (`builder_inheritance.py`)

When builders form a **hierarchy** (each level adds more capabilities), each builder extends the previous one.

* `PersonBuilder` → `PersonInfoBuilder` (adds `called()`) → `PersonJobBuilder` (adds `works_as_a()`).
* Because each builder returns `self`, the most derived builder can chain all methods from all levels:
  ```python
  pb.called("John").works_as_a("Software Engineer").build()
  ```
* **Rule of thumb:** order the inheritance chain from most general to most specific.

---

### When to Use the Builder Pattern

* Object has **many optional or grouped parameters** (avoids telescoping constructors).
* Construction requires **multiple steps** or a specific sequence.
* You want the **same construction process** to produce different representations.
* You need to **hide internal complexity** from client code.

---

### Real-World Examples

| Scenario | Product | Builder role |
|---|---|---|
| **SQL query construction** | A `SELECT` query string | `.select("name").from_table("users").where("age > 21").order_by("name")` — avoids messy string concatenation and SQL injection risks |
| **HTTP request setup** | An `HttpRequest` object | `.url("/api/data").header("Auth", token).body(json).timeout(30).build()` — common in REST clients |
| **CI/CD pipeline config** | A pipeline definition | `.stage("build").step(compile).stage("test").step(unit).step(integration).build()` — each stage/step added incrementally |
| **UI form / document generation** | A PDF or HTML report | Add title, sections, tables, footers step-by-step; same builder can output PDF or HTML (different representations) |
| **Cloud infrastructure (IaC)** | A VM / container spec | `.image("ubuntu").cpu(4).memory("16GB").disk("100GB").network(vpc).build()` — used in SDKs like AWS CDK, Pulumi |

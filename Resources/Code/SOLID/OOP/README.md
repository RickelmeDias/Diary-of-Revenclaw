## Quick Review about OOP

###

- [Cohesion](#cohesion)
- [Coupling](#coupling)
- [Encapsulation](#encapsulation)
- [Good Links To Improve!](#links-good-to-improve)

### Cohesion

Cohesion refers to what the class (or module) can do.

It is about the attributes and methods inside a class it needs to be in harmony, representing things in common, then in the cohesion is important a class to have a high cohesion.

- **Low cohesion** would mean that the class **does a great variety of actions** - **it is broad, unfocused on what it should do**.
- **High cohesion** means that the class **is focused on what it should be doing**, i.e. only methods relating to the intention of the class.

```
Low Cohesion

-------------------
| Staff           |
-------------------
| checkEmail()    |
| sendEmail()     |
| emailValidate() |
| PrintLetter()   |
-------------------


High Cohesion

---------------------------
| Staff                   |
---------------------------
| -salary                 |
| -emailAddr              |
---------------------------
| setSalary(newSalary)    |
| getSalary()             |
| setEmailAddr(newEmail)  |
| getEmailAddr()          |
---------------------------
```

Example of a **High Cohesion** class using Java:

```java
    public class Employee {
        private String name;
        private String document;
        private Position position;
        private BigDecimal salary;

        public boolean isManager() {
            return Position.MANAGER == this.position;
        }
    }
```

Example of a **Low Cohesion** class using Java, this class do many things, a probably improve should be create a new class for Address:

```java
    public class Employee {
        private String name;
        private String document;
        private Position position;
        private BigDecimal salary;
        private String zipCode;
        private String street;
        private String neighborhood;
        private String city;
        private String state;

        public boolean isManager() {
            return Position.MANAGER == this.position;
        }

        public void formatDocument() {
            // ... format Document
        }

        public void validateAddress() {
            // ... validate Address
        }
    }
```

So, we will maintain the classes with High Cohesion, because classes without a good Cohesion or with a low Cohesion tend to grow indefinitely, which makes them difficult to maintain.

### Coupling

Coupling is when two components are coupling, creating a dependency on each other. If a class A uses class B, it is an example of coupling, coupling is normal and necessary for codes, but a tight coupling can be bad, because some classes know very deep and a lot about another class, creating a strong dependency. When changing something in class B, if it has a strong dependency, class A will likely have a problem and break all code that uses class A.

Example, good coupling:

```java
Employee emp = loadFromDatabase();
BigDecimal totalChanges = emp.getSalaryChanges();
```

Bad coupling:

```java
Employee emp = loadFromDatabase();

BigDecimal totalChanges = 0;

List<SalaryChanges> salaryChanges = emp.getSalaryChanges();
for (SalaryChanges s : salaryChanges) {
    totalChanges += s.getValue();
}
```

If in the future is need to change something in the Employee class, like change the `list` to `map`, it will break this strong coupling.

Not knowing how to deal with coupling can make several classes depend heavily on other classes, when one of them breaks it will break the other, generating a sequence of errors and corrections.

### Encapsulation

The encapsulation is protect a class against external influences and manipulations that could harm the information consistence.

A good example of the encapsulation concept:

```java
    public class Employee {
        private String name;
        private String document;
        private Position position;
        private BigDecimal salary;

        public void wageAdjustment (BigDecimal increase) {
            BigDecimal percentual = (increase/salary)*100;

            if (percentual > 25) {
                throw new IllegalArgumentException(
                    "Percentage of the wage adjustment must be less than 25%"
                );
            }
            this.salary += increase;
        }
    }
```

A bad example of the encapsulation concept, because in this case setSalary allows us to receive all values without security or protection, which allows the violation of the business rule, see:

```java
    public class Employee {
        private String name;
        private String document;
        private Position position;
        private BigDecimal salary;

        public void setSalary (BigDecimal salary) {
            this.salary = salary;
        }
    }
```

### Links good to improve:

- [How to explain object-oriented programming concepts to a 6-year-old](https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/)
- [Difference between Cohesion and Coupling](https://stackoverflow.com/questions/3085285/difference-between-cohesion-and-coupling)
- [Why use getters and setters/accessors](https://stackoverflow.com/questions/1568091/why-use-getters-and-setters-accessors)
- [How is encapuslation broken by getters and setters](https://softwareengineering.stackexchange.com/questions/297488/how-is-encapsulation-broken-by-getters-setters-even-when-using-mvc-model)
- [When are Getters and Setters Justified](https://softwareengineering.stackexchange.com/questions/21802/when-are-getters-and-setters-justified)

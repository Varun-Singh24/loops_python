## 🔄 Control Flow: Loops & Break Statements

### This repository focuses on **Iterative Logic** in Python. It demonstrates how to use `for` and `while` loops to solve mathematical problems and how to use the `break` keyword to control loop execution.

### Mastery of loops is the foundation of **Algorithm Design** and **Problem Solving**.

---

## 🛠️ Tools & Environment

* **Language:** Python 🐍
* **Environment:** Jupyter Notebook / VS Code
* **Concepts Used:** - `for` loops with `range()`
* `while` loops with conditions
* `break` statements for early exit
* Floor Division (`//`) and Modulo (`%`) operators



---

## 🛑 Sum with Early Break

### 📌 Concept

Calculating the sum of natural numbers but stopping immediately once a specific threshold (limit) is reached using the `break` statement.

### 🧾 Code

```python
number = 20  # Limit for range
total_sum = 0  

print("Iterating to find sum (Max Limit: 30):")
for i in range(1, number): 
    total_sum += i 
    if total_sum > 30: 
        print(f"--- Limit Reached! Sum: {total_sum} ---")
        break
    print(f"Number: {i}, Running Sum: {total_sum}")

```

### 📘 Explanation

* **`total_sum += i`**: Adds the current number to the running total.
* **`break`**: This "emergency exit" stops the loop entirely when the condition (`> 30`) is met, even if the range isn't finished.

---

## ⏳ Dynamic Summation (While Loop)

### 📌 Concept

Using a `while` loop to continue adding numbers until the sum reaches a user-defined input.

### 🧾 Code

```python
limit = int(input("Enter the target sum: "))
current_sum = 0 
i = 1 

while current_sum < limit: 
    print(f"Adding {i} | Total: {current_sum}") 
    current_sum += i
    i += 1 

```

### 🎯 Use Case

✔ Useful when you don't know how many iterations you need (unlike `for` loops).
✔ Perfect for event-driven programming (waiting for a condition to change).

---

## 🔃 Reversing a Number (Mathematical Approach)

### 📌 Concept

To reverse a number without using string slicing, we use the **Modulo** (`%`) to get the last digit and **Floor Division** (`//`) to remove it.

### 🧾 Code

```python
num = int(input("Enter a number to reverse: "))
reverse = 0

while num > 0:
    last_digit = num % 10          # Get the last digit
    reverse = (reverse * 10) + last_digit  # Build the reversed number
    num = num // 10                # Remove the last digit
    
print(f"Reversed Number: {reverse}")

```

### 📘 Explanation

* **`num % 10`**: Grabs the remainder (e.g., `123 % 10 = 3`).
* **`num // 10`**: Performs integer division to drop the decimal (e.g., `123 // 10 = 12`).
* **`reverse * 10`**: Shifts the current digits to the left to make room for the new one.

---

## 🧠 Concepts Practiced 

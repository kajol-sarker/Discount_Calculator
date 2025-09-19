# 💰 Discount Calculator

### Project Overview
This is a simple Python program to calculate discounts on a bill. It is a beginner-friendly exercise designed to demonstrate the effective use of **conditional statements** (`if`, `elif`, and `else`) in Python. The program simulates a basic tiered discount system for a retail store.

### ✨ Features
* **User-Friendly Input:** Prompts the user to enter the total bill amount.
* **Tiered Discounts:** Applies different discount rates based on the total bill amount.
* **Clear Output:** Displays the calculated discount amount and the final price with precise formatting.

### ⚖️ Discount Policy
| Bill Amount Range | Discount Applied |
| :--- | :--- |
| > ৳1000 | 20% |
| > ৳500 | 10% |
| ≤ ৳500 | No Discount |

### 🚀 How to Run
1.  Save the code as a Python file (e.g., `discount_calculator.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the program using the following command:
    ```bash
    python discount_calculator.py
    ```

### 📜 Example Usage
* **Bill over ৳1000:**
    *Input:* `1250`
    *Output:* `Final Bill: 1000.00 taka`

* **Bill between ৳501 and ৳1000:**
    *Input:* `780`
    *Output:* `Final Bill: 702.00 taka`

* **Bill ৳500 or less:**
    *Input:* `450`
    *Output:* `Final Bill: 450.00 taka`

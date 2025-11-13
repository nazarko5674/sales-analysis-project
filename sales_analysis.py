import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Генеруємо випадкові дані про продажі
np.random.seed(42)
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'sales': np.random.randint(1000, 5000, 6),
    'expenses': np.random.randint(500, 3000, 6)
}

df = pd.DataFrame(data)

# Додаємо прибуток
df['profit'] = df['sales'] - df['expenses']

# Виводимо таблицю
print("Sales Data:")
print(df)

# Будуємо графік
plt.plot(df['month'], df['sales'], label='Sales', marker='o')
plt.plot(df['month'], df['expenses'], label='Expenses', marker='x')
plt.plot(df['month'], df['profit'], label='Profit', marker='s')

plt.title('Monthly Sales Analysis')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.show()

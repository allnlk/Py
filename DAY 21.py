class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        total = 0
        for x in self.data:
            total += x
        return total

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) // 2
        else:
            return sorted_data[mid]

    def mode(self):
        freq = {}

        for x in self.data:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        max_count = max(freq.values())

        for key, value in freq.items():
            if value == max_count:
                return (key, value)

    def var(self):
        m = self.mean()
        total = 0

        for x in self.data:
            total += (x - m) ** 2

        return round(total / self.count(), 1)

    def std(self):
        return round(self.var() ** 0.5, 1)

    def freq_dist(self):
        freq = {}

        for x in self.data:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        result = []
        total = self.count()

        for key, value in freq.items():
            percent = round((value / total) * 100, 1)
            result.append((percent, key))

        result.sort(reverse=True)
        return result

    def describe(self):
     print("Count:", self.count())
     print("Sum: ", self.sum())
     print("Min: ", self.min())
     print("Max: ", self.max())
     print("Range: ", self.range())
     print("Mean: ", self.mean())
     print("Median: ", self.median())
     print("Mode: ", self.mode())
     print("Variance: ", self.var())
     print("Standard Deviation: ", self.std())
     print("Frequency Distribution:", self.freq_dist())

ages = [
    31, 26, 34, 37, 27, 26, 32, 32, 26, 27,
    27, 24, 32, 33, 27, 25, 26, 38, 37, 31,
    34, 24, 33, 29, 26
]

data = Statistics(ages)

print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())

print("\nDescribe:")
data.describe()


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = f"Name: {self.firstname} {self.lastname}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Balance: {self.account_balance()}\n"
        info += "Income Details:\n"
        for desc, amount in self.incomes.items():
            info += f"  {desc}: {amount}\n"
        info += "Expense Details:\n"
        for desc, amount in self.expenses.items():
            info += f"  {desc}: {amount}\n"
        return info

person = PersonAccount("Alice", "Smith")
person.add_income("Salary", 3000)
person.add_income("Freelance", 800)
person.add_expense("Rent", 1200)
person.add_expense("Food", 400)
person.add_expense("Transport", 150)
print(person.account_info())
print("Account Balance:", person.account_balance())

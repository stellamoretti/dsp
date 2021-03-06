# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in the following ways:
>> - Each is a sequence of values.
>> - The values can be any type.
>> - The values are indexed by integers.
>>
>> Lists and tuples are different in the following ways:
>> - A list is mutable (its values can be changed) whereas a tuple is immutable (its values cannot be changed once created).
>> - Lists are homogeneous sequences (i.e. have order) and Tuples are heterogeneous data structures (i.e. are structured).
>> - Syntactically, lists are enclosed within square brackets and tuples are enclosed within parentheses.
>>
>> A dictionary is implemented using a hashtable, which means that its keys have to be "hashable" (i.e. mutable). Hence, lists may be used as keys but tuples cannot.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in the following ways:
>> - Each is a sequence of values.
>> - They are both iterable (e.g. can be accessed using a `for` loop).
>>
>> Lists and sets are different in the following ways:
>> - Lists are ordered whereas sets are unordered.
>> - Lists may contain duplicate items, whereas the elements in a set are unique.
>> - List values are indexed whereas set items cannot be accessed by index.
>> - A list is mutable (its values can be changed) whereas a set is immutable (its values cannot be changed once created).
>> - Syntactically, lists are enclosed within square brackets and sets are enclosed within curly brackets.

>> Comparing performance:  
>> If iterating over a sequence of values, Python perform slower than lists because they use a hashtable as their underlying data structure.  However if checking the existence of a value in a sequence, this can be performed faster with a set in which the elements are unique.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` expressions are small anonymous functions which behave just like regular functions but are syntactically restricted to a single expression. They can be used wherever function objects are required, and are commonly used in conjunction with `filter()`, `map()` and `reduce()` functions.
>>  
>> Example 1:  
>> ```
>> >>> (lambda x,y: x * y)(2,3)  
>> 6
>> ```  
>>  
>> Example 2:  
>> ```
>> >>> sorted([9,0,-99,98,6,15,-1,-55], key=lambda x: abs(x))  
>> [0, -1, 6, 9, 15, -55, 98, -99]
>> ```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions provide a concise way to create lists. A list comprehension consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result will be a new list resulting from evaluating the expression in the context of the `for` and `if` clauses which follow it.  
>>  
>> The simplest form of a list comprehension is:  
>> `[expression-involving-loop-variable for loop-variable in sequence]`  
>> A filtered list comprehension will be structured in the following way:  
>> `[expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable]`
>>  
>> __Example 1: Filtering a list__  
>>  
>> Usual way:  
>> ```
>> >>> numbers = [1,5,6,9,10,11,15,16]  
>> >>> divisible_by_3 = []  
>> >>> for num in numbers:  
>> >>>     if num % 3 == 0:  
>> >>>         divisible_by_3.append(num)  
>> >>> return divisible_by_3  
>> ```
>> Using list comprehension:  
>> ```
>> >>> [num for num in numbers if num % 3 == 0]
>> ```
>> __Example 2: Mapping a function__  
>>  
>> Usual way:  
>> ```
>> >>> numbers = [1,2,3,4,5,6]  
>> >>> squared = []  
>> >>> for num in numbers:  
>> >>>     squared.append(num ** 2)
>> >>> return squared  
>> ```
>> Using list comprehension:  
>> ```
>> >>> [num ** 2 for num in numbers]
>> ```
>> __Example 3: Dictionary comprehension__  
>>  
>> Usual way:  
>> ```
>> >>> numbers = [1,2,3,4,5,6]  
>> >>> squared = {}  
>> >>> for num in numbers:  
>> >>>     squared.update({num: num ** 2})
>> >>> return squared  
>> ```
>> Using dictionary comprehension:  
>> ```
>> >>> {num: num ** 2 for num in (1,2,3,4,5,6)}  
>> ```
>> __Example 4: Set comprehension__  
>>  
>> Usual way:  
>> ```
>> >>> numbers = [1,2,3,4,5,6,1,2]  
>> >>> squared = set()
>> >>> for num in numbers:  
>> >>>     squared.add(num ** 2)
>> >>> return squared  
>> ```
>> Using set comprehension:  
>> ```
>> >>> {num ** 2 for num in numbers}  
>> ```
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)

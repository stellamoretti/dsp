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
>> - They can both be accessed using a `for` loop.
>>
>> Lists and sets are different in the following ways:
>> - Lists are ordered whereas sets are unordered.
>> - Lists may contain duplicate items, whereas the elements in a set are unique.
>> - List values are indexed whereas set items cannot be accessed by index.
>> - A list is mutable (its values can be changed) whereas a set is immutable (its values cannot be changed once created).
>> - Syntactically, lists are enclosed within square brackets and sets are enclosed within curly brackets.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

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






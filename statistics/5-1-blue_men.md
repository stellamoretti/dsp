[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Convert heights from feet/inches to centimeters:
```python
upper = 6 * 30.48 + 1 * 2.54
lower = 5 * 30.48 + 10 * 2.54
print(upper, lower)
```  
Yields:  
185.42 177.8  
  
Use the CDF to evaluate the percentage of US males who are in this range:  
```python
dist.cdf(upper) - dist.cdf(lower)
```
  
**Answer:**  
For some reason my answer comes out differnt to the actual answer(?)  
1.0304925738724435e-05

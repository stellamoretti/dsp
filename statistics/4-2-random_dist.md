[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

Generate 1000 numbers from numpy:  
`x = np.random.random(1000)`  
  
Plot the PMF:
```python
pmf = thinkstats2.Pmf(x, label='numbers')
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='number', ylabel='Pmf')
```  
_What goes wrong?_
  
Every value has the same probability.
  
Plot the CDF:
```python
cdf = thinkstats2.Cdf(x, label='numbers')
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='number', ylabel='CDF')
```  
  
_Is the distribution uniform?_
  
Yes - as shown by the straight line CDF.

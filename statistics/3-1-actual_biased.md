[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Load the respondent file:
>> `resp = nsfg.ReadFemResp()`
>> Create a Pmf object:
>> `pmf = thinkstats2.Pmf(resp.numkdhh, label='actual (numkdhh)')`
>> Plot the PMF as a step function:
>> `thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='number of children', ylabel='Pmf')
`
>> Call the `BiasPmf` function to compute the biased PMF:
>> `biased_pmf = BiasPmf(pmf, label='observed (biased)')`
>> Plot the biased PMF:
>> ```
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='number of children', ylabel='PMF')
```
>> Calculate the actual and observed means:
>> `print('Actual mean', pmf.Mean())
print('Observed mean', biased_pmf.Mean())
`
>> Solution:
>> Actual mean 1.02420515504
>> Observed mean 2.40367910066

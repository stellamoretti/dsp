[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> __Comparing the weight of first babies to other babies__  
>>  
>> Mean birthweights of each group:  
>> ```firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()```  
>> _Answer:_  
>> (7.201094430437772, 7.325855614973262)
>>
>> Difference between the means of the two groups:  
>> ```firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()```  
>> _Answer:_  
>> -0.12476118453549034 lbs
>>
>> ```CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)```  
>> _Answer:_  
>> -0.088672927072602006 standard deviations
>>
>> __Discussion:__
>> First babies are lighter than others but the difference in means is 0.09 standard deviations, which is small.
>> This result seems to correlate with the earlier discovery that first babies have a shorter pregnancy length, and hence, less time to grow.

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 23:45:26 2018

@author: devar
"""

import pandas as pd
url = "G:\\MSIT\\specializations\\assign\\wikisubset"


links = pd.read_csv(url +"\\links.tsv", sep='\t', comment='#', names=['source', 'target'])
links


smatrix = [line for line in open(url+'\\shortest-path-distance-matrix.txt').read().split('\n') if (line and not line.startswith('#'))]
smatrix

           
articles = [line for line in open(url + '\\articles.tsv').read().split('\n') if (line and not line.startswith('#'))]
articles



from collections import Counter

indegree = Counter(links['target'])
for xx in indegree.most_common(2):print(xx)
print('='*120)


closeness = dict()
for jj, article in enumerate(articles):
    ans = 0
    for i in range(len(smatrix)):
        cur = smatrix[i][jj]
        
        if cur == '_':
            cur = '10'
        ans+=int(cur)
    closeness[article] = (len(smatrix)-1)/ans
closeness = Counter(closeness)


print('Closeness')
for xx in closeness.most_common(25): print(xx)
print('='*120)
    
print(closeness.most_common(25))


alpha = 0.95
max_niterations = 100
tolerance = 0.000001
outdegrees = Counter(links['source'])

pagerank = dict()
n = len(articles)
for x in articles:
    pagerank[x] = 0

damp = (1 - alpha) / n


# pagerank: iterations
for iteration in range(max_niterations):
    print('Iteration number: ', iteration)
 
    # calculate    
    new_pagerank = dict()
    for x in articles:
        new_pagerank[x] = 0
        
    for source, target in zip(links['source'], links['target']):
        old = pagerank[source] if pagerank[source] != 0 else 1/n
        new_pagerank[target] += old/outdegrees[source]
        
    for xx in new_pagerank:
        new_pagerank[xx] = damp + alpha * new_pagerank[xx]
 
    # termination criteria 
    max_delta = max(abs(new_pagerank[xx]-pagerank[xx]) for xx in pagerank.keys())

    if max_delta < tolerance:
        break
 
    # update
    pagerank = new_pagerank

 
pagerank = Counter(pagerank)
 
print('Pagerank')
for xx in pagerank.most_common(25): print(xx)
print('='*120)





indegree.most_common(5)
indegrees_index = dict((xx, ii) for ii, (xx, ss) in enumerate(indegree.most_common()))
closeness_index = dict((xx, ii) for ii, (xx, ss) in enumerate(closeness.most_common()))
pagerank_index = dict((xx, ii) for ii, (xx, ss) in enumerate(pagerank.most_common()))
 
selected = [
    'Adolf_Hitler',
    'Albert_Einstein',
    'Algorithm',
    'Arnold_Schwarzenegger',
    'Australia',
    'Atom',
    'Azerbaijan',
    'Australian_Open',
    'American_football',
    'Alexander_Graham_Bell',
    'Astronomy',
    'Asteroid',
    'Arugula',
    'Asparagus',
    'Amsterdam',
    'Abraham_Lincoln',
]
 
print ('Ranked by indegrees', sorted(selected, key=indegrees_index.get))
print ('Ranked by closeness', sorted(selected, key=closeness_index.get))
print ('Ranked by pagerank' , sorted(selected, key=pagerank_index.get))


























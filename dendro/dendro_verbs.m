man_file = 'out_verbs_man'
woman_file = 'out_verbs'

A = importdata(man_file)
At = transpose(A)
[R,P] = corrcoef(At)
tree = linkage(R,'average')

xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'},
dendrogram(tree,0,'labels',xlabs)

ylabel('Distance');
title('Dendrogram of clustered correlation matrix -- similarity of male words to various verbs across 22 corpora')

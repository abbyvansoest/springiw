A = importdata('out_adj_s')

xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'}

Y = pdist(A)
squareform(Y)
Z = linkage(Y, 'ward') % ward is pretty good or maybe single

% quality of results
cope = cophenet(Z,Y)

c = cluster(Z,'maxclust',6)

Q = cmdscale(Y);

gscatter(Q(:,1),Q(:,2),c)
legend(gca,'off')
text(Q(:,1), Q(:,2), xlabs, 'horizontal','left', 'vertical','bottom')

%figure;dendrogram(Z,0,'labels',xlabs)



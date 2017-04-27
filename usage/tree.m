A = importdata('usage_sim_jac')
% At = transpose(A)
% [R,P] = corrcoef(At)
fig = linkage(A,'complete')
xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'},
figure;dendrogram(fig,0,'labels',xlabs)
% ylabel('Distance');
% title('Similarity of gendered words to various occupations across 22 corpora')
% 
c = cluster(fig,'maxclust',3);
size(c)
size(fig)
scatter(A(:,1),A(:,2), 10, c)
% 
%text(fig(:,1), fig(:,2), fig(:,3), xlabs, 'horizontal','left', 'vertical','bottom')

% idx = kmeans(A,3)
% 
% figure;
% plot(A(idx==1,1),A(idx==1,2),'r.','MarkerSize',12)
% hold on
% plot(A(idx==2,1),A(idx==2,2),'b.','MarkerSize',12)
% hold on
% plot(A(idx==3,1),A(idx==3,2),'c.','MarkerSize',12)
% 
% text(A(:,1), A(:,2), xlabs, 'horizontal','left', 'vertical','bottom')


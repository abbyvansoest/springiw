man_file_adj = 'out_adj_m'
woman_file_adj = 'out_adj_w'
s_file_adj = 'out_adj_s'

man_file_verb = 'out_verbs_m'
woman_file_verb = 'out_verbs_w'
s_file_verb = 'out_verbs_s'

A = importdata(woman_file_verb);
At = transpose(A);
[R,P] = corrcoef(At)
tree = linkage(R,'weighted');   % average, ward or weighted
xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'};
figure;dendrogram(tree,0,'labels',xlabs);
% % ylabel('Distance');
% % title('HI')

save('w_verb_corr','R', '-ascii');

% cg = clustergram(At, 'Cluster','row','Linkage', 'ward', 'Colormap','redbluecmap(20)','DisplayRatio',[.55 .45])
% set(cg, 'ColumnLabels',xlabs);
% cg2 = clustergram(At, 'Linkage', 'ward', 'Colormap','redbluecmap(20)')
% set(cg2, 'ColumnLabels',xlabs);
% 

% A = importdata(s_file_verb)
% At = transpose(A)
% [R,P] = corrcoef(At)
% tree = linkage(R,'average')
% xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'},
% figure;dendrogram(tree,0,'labels',xlabs)
% ylabel('Distance');
% title('Similarity of gendered words to various verbs across 22 corpora')
% 
% save('s_verb_corr','R', '-ascii');
% 
% A = importdata(woman_file_adj)
% At = transpose(A)
% [R,P] = corrcoef(At)
% tree = linkage(R,'average')
% xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'},
% dendrogram(tree,0,'labels',xlabs)
% ylabel('Distance');
% title('Similarity of female words to various adjectives across 22 corpora')
% 
% save('woman_adj_corr','R', '-ascii');
% 
% A = importdata(woman_file_verb)
% At = transpose(A)
% [R,P] = corrcoef(At)
% tree = linkage(R,'average')
% xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'},
% figure;dendrogram(tree,0,'labels',xlabs)
% ylabel('Distance');
% title('Similarity of female words to various verbs across 22 corpora')
% 
% save('woman_verb_corr','R', '-ascii');
% 
% A = importdata(man_file_adj)
% At = transpose(A)
% [R,P] = corrcoef(At)
% tree = linkage(R,'average')
% xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'},
% dendrogram(tree,0,'labels',xlabs)
% ylabel('Distance');
% title('Similarity of male words to various adjectives across 22 corpora')
% 
% save('man_adj_corr','R', '-ascii');
% 
% A = importdata(man_file_verb)
% At = transpose(A)
% [R,P] = corrcoef(At)
% tree = linkage(R,'average')
% xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'},
% figure;dendrogram(tree,0,'labels',xlabs)
% ylabel('Distance');
% title('Similarity of male words to various verbs across 22 corpora')
% 
% save('man_verb_corr','R', '-ascii');

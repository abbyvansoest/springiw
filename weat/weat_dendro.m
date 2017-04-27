A = importdata('weat-data2.txt');
At = A;
%A = importdata('expanded-weat-data.txt');
%At = transpose(A);
[R,P] = corrcoef(At);
tree = linkage(R,'average');  
xlabs = {'AU', 'BD', 'CA','GBB','GBG','GH','HK','IE','IN','JM','KE','LK','MY','NG','NZ','PH','PK','SG','TZ','USB','USG','ZA'};
figure;dendrogram(tree,0,'labels',xlabs);

ylabel('Distance');

save('weat-exp-corr','R','-ascii')
import matplotlib.pyplot as plt
plt.title('Accuracy for Random Forest over 5 devices and 3 users on Testing Data',fontsize=24)
plt.plot(['nexus1_user_c','nexus2_userb,','nexus2_userc','s3_usera','s3_userb','s3_userc','s3_2_usera','s3_2_userb','s3_2_userc','s3mini1_usera','s3mini1_userb','s3mini1_userc'], [83.38,86.9346,77.868166,84.135,85.9457128,83.4581,82.60486,80.932,83.458,87.531,82.604,84.614],'ro')
plt.ylabel('Accuracy percentage',fontsize=18)
plt.xlabel('Device models_corresponding users',fontsize=18)
plt.axis([0,13,0,100],fontsize=20)
#plt.savefig('books_read.png')
plt.show()



import matplotlib.pyplot as plt
plt.title('Accuracy for Logistic Regression',fontsize=24)
plt.plot(['nexus1_user_c','nexus2_userb,','nexus2_userc','s3_usera','s3_userb','s3_userc','s3_2_usera','s3_2_userb','s3_2_userc','s3mini1_usera','s3mini1_userb','s3mini1_userc'], [83.33,82.5,83.319,84.135,83.33333333333333,83.13,84.54,83.33,84.458,83.31,82.604,84.0],'ro')
plt.ylabel('Accuracy percentage',fontsize=18)
plt.xlabel('Device models_corresponding users',fontsize=18)
plt.axis([0,13,0,100],fontsize=20)
#plt.savefig('books_read.png')
plt.show()



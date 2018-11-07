import matplotlib.pyplot as plt
plt.title('Accuracy for Random Forest over 5 devices and 3 users on Training dataset to crosscheck',fontsize=24)
plt.plot(['nexus1_user_c','nexus2_userb,','nexus2_userc','s3_usera','s3_userb','s3_userc','s3_2_usera','s3_2_userb','s3_2_userc','s3mini1_usera','s3mini1_userb','s3mini1_userc'], [99.075,99.082509,98.695036,99.041,98.99,98.86,99.05,98.792,98.97085,99.1127919,99.0101615,99.0614528],'ro')
plt.ylabel('Accuracy percentage',fontsize=18)
plt.xlabel('Device models_corresponding users',fontsize=18)
plt.axis([0,13,0,100],fontsize=20)
#plt.savefig('books_read.png')
plt.show()



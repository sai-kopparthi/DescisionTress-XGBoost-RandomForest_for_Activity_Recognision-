import matplotlib.pyplot as plt
plt.title('Accuracy for XGBoost over 5 devices and 3 users',fontsize=24)
plt.plot(['nexus1_user_b','nexus1_user_c','nexus2_userb,','nexus2_userc','s3_usera','s3_userb','s3_userc','s3_2_usera','s3_2_userb','s3_2_userc','s3mini1_usera','s3mini1_userb','s3mini1_userc'], [79.45,82.82,77.43,83.69,85.84,80.95,83.59,86.09,81.41,83.73,85.85,81.31,83.08])
plt.ylabel('Accuracy percentage',fontsize=18)
plt.xlabel('Device models_corresponding users',fontsize=18)
plt.axis([0,13,0,100],fontsize=20)
#plt.savefig('books_read.png')
plt.show()



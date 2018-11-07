import matplotlib.pyplot as plt
plt.title('Accuracy for Knearest neighbours',fontsize=24)
plt.plot(['nexus1_user_c','nexus2_userb,','nexus2_userc','s3_usera','s3_userb','s3_userc','s3_2_usera','s3_2_userb','s3_2_userc','s3mini1_usera','s3mini1_userb','s3mini1_userc'], [78.5,80.0,81.1,83.7,77.20,80.0,82.20,78.30,82.5,85.2,82.8,81.2],'ro')
plt.ylabel('Accuracy percentage',fontsize=18)
plt.xlabel('Device models_corresponding users',fontsize=18)
plt.axis([0,13,0,100],fontsize=20)
#plt.savefig('books_read.png')
plt.show()



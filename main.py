
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url_data = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
class drawing():
    def __init__(self, url_data):
        self.df = pd.read_json(url_data)


    def draw_plots(self):

          # Let's compare two values ("ceiling_mean" and "floor_mean"): 
        x = self.df.ceiling_mean
        y = self.df.floor_mean
        plt.scatter(x, y)
        plt.savefig('/Users/antonovegor/Downloads/Project/venv/plots/1.png')
        plt.show() 

           # Lets try to approximate their dependence using linear function as we see in the graph above:
        s = np.polyfit(x,y,1)
        y_1 = s[0] * x + s[1] 
        plt.scatter(x, y)
        plt.plot(x, y_1, color="red")
        plt.savefig('/Users/antonovegor/Downloads/Project/venv/plots/2.png')

          # We can see that with the growth of rb_corners,  rb_corners, 
          # the values of "ceiling_men" and "floor_mean" increase like this:
        plt.plot([4, 6, 8], [9.856579158486156, 17.74685519936543, 23.588692605399995])
        plt.savefig('/Users/antonovegor/Downloads/Project/venv/plots/3.png')
        plt.show()
        

          # Now about "gt_corners" and "mean" dependence:
        x_2 = df[df.gt_corners == 4]["mean"]
        x_2 = list(x_2)
        x_3= df[df.gt_corners == 6]["mean"]
        x_3 = list(x_3)
        x_4= df[df.gt_corners == 8]["mean"]
        x_4 = list(x_4)
        plt.hist(x_2)
        plt.hist(x_3, color = "red")
        plt.hist(x_4, color = "yellow")
        plt.savefig('/Users/antonovegor/Downloads/Project/venv/plots/4.png')
        plt.show()
        

          # Let's look at the dependence of the maximum and minimum:
        plt.scatter(df.ceiling_min, df.ceiling_max)
        plt.savefig('/Users/antonovegor/Downloads/Project/venv/plots/5.png')
        plt.show()
        plt.scatter(df.floor_min, df.floor_max, color = "red")
        plt.savefig('/Users/antonovegor/Downloads/Project/venv/plots/6.png')

        a = [f"/Users/antonovegor/Downloads/Project/venv/plots/{i}.png" for i in range(1, 7)]
        return a 

example = drawing(url_data)
example.draw_plots()
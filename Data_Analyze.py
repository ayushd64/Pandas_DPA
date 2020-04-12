from Data_Clean import Data_Clean
class Data_Analyze(Data_Clean):
    import matplotlib.pyplot as plt
    from IPython.display import display
    import seaborn as sn
    
    def __init__(self):
        super().__init__()
        self.data = super().data_cleaning()
        self.train_data = self.data[0]
        self.test_data = self.data[1] 

    def graph_1(self):
        ax = self.train_data['Age'].value_counts().sort_index().plot(kind = 'bar')
        ax.set(ylabel = "No. of players")
        ax.set(xlabel = "Age")
        self.plt.show()
    
    def graph_2(self):
        ax = self.train_data.groupby("Age")["Overall Rating"].mean().plot(marker = "o")
        ax.set(ylabel = "Avg. Overall Rating")
        self.plt.show()
    
    def graph_3(self):
        ax = self.train_data.groupby("Age")["Best Overall"].mean().plot(marker = "o")
        ax.set(ylabel = "Avg. Best Overall")
        self.plt.show()
    
    def graph_4(self):
        ax = self.train_data.groupby("Age")["Total potential"].mean().plot(marker = "o")
        ax.set(ylabel = "Avg. Total potential")
        self.plt.show()
    
    def graph_5(self):
        ax = self.train_data.groupby("Age")["Skill sets"].mean().plot(marker = "o")
        ax.set(ylabel = "Avg. Skill sets")
        self.plt.show()
    
    def graph_6(self):
        ax = self.train_data.groupby("Age")["Power stats"].mean().plot(marker = "o")
        ax.set(ylabel = "Avg. Power stats")
        self.plt.show()
    
    def graph_7(self):
        ax = self.train_data.groupby("Age")["Defence stats"].mean().plot(marker = "o")
        ax.set(ylabel = "Avg. Defence stats")
        self.plt.show()
        
    def data_description(self):
        describe = self.train_data.describe()
        self.display(describe)
    
    def cor_matrix(self):
        self.cor = self.train_data.corr()
        self.plt.figure(figsize = (10,5))
        return self.cor
    
    def all_graphs(self):
        self.graph_1()
        self.graph_2()
        self.graph_3()
        self.graph_4()
        self.graph_5()
        self.graph_6()
        self.graph_7()
        self.sn.heatmap(self.cor_matrix(), annot=True)
        self.display(self.cor_matrix())
        self.data_description()
        return self.train_data, self.test_data
        
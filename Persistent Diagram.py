from gtda.plotting import plot_diagram

class TDA:
    def plot_graph(diagrams):
        return plot_diagram(diagrams[0])

if __name__ == '__main__':
    #Get the csv that containing the ph results (given by the py file PHGeneration.py)
    result_1 = pd.read_csv("test.csv")
    #Choose a certain label for reference (choosing a certain distance cutoff)
    result_selected = result_1[result_1['label'] == 50]
    diagram = result_selected[["birth", "death", "dimension"]].values
    TDA.plot_graph([np.array(diagram)])
    # a diagram will be returned
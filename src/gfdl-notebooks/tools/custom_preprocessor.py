import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

class StopExecutionPreprocessor(ExecutePreprocessor):
    def preprocess_cell(self, cell, resources, cell_index):
        if 'stop_here' in cell.metadata.get('tags', []):
            raise CellExecutionError("Stopping execution", "stop_here tag found", "")
        return super().preprocess_cell(cell, resources, cell_index)

def execute_notebook(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    ep = StopExecutionPreprocessor(timeout=None, kernel_name='python3')
    try:
        ep.preprocess(nb, {'metadata': {'path': './'}})
    except CellExecutionError as e:
        print(e)
    with open(notebook_path, 'w') as f:
        nbformat.write(nb, f)

if __name__ == "__main__":
    import sys
    execute_notebook(sys.argv[1])

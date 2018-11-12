from tf import TFNode, TFTree, Transform
from pprint import pprint
import numpy as np

### Transform tests

def test_transform():
    x = Transform.from_position_euler(0, 0, 0, 3.141, 0, 0)

def test_tree():
    tree = TFTree()
    tree.add_transform('map', 'odom', Transform(1, 1, 1, 0, 0, 0, 1))
    tree.add_transform('odom', 'camera1', Transform.from_position_euler(0, 0, 0, np.pi, 0, 0))

    print tree.lookup_transform('camera1', 'map').euler

    tree.add_transform('camera1', 'camera2', Transform.from_position_euler(0, 0, 0, np.pi, 0, 0))

    print tree.lookup_transform('camera2', 'map').euler

    pprint(tree.to_dict())

    pprint(TFTree.from_dict(tree.to_dict()).to_dict())

if __name__ == '__main__':
    test_transform()

    test_tree()

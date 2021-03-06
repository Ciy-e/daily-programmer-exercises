public class BinarySearchTree {
    Node root;

    private class Node {
        Node left;
        Node right;
        int data;

        public Node(int data){
            this.data = data;
            this.right = null;
            this.left = null;
        }

        public int getData() {
            return this.data;
        }
        
    }

    public BinarySearchTree(int[] data) {
        for(int i: data) {
            this.addElement(i);
        }
    }

    public void addElement(int data) {
        if (this.root == null) {
            this.root = new Node(data);
        } else {
            boolean added = false;
            Node cur = this.root;
            while (!added) {
                if (cur.data > data) {
                    if(cur.left == null) {
                        cur.left = new Node(data);
                        added = true;
                    } else {
                        cur = cur.left;
                    }
                } else {
                    if(cur.right == null) {
                        cur.right = new Node(data);
                        added = true;
                    } else {
                        cur = cur.right;
                    }
                }
            }

        }

    }

    // preOrder tree traversal
    public static void preOrder(Node root) {
        Node currentNode = root;
        System.out.print(currentNode.data + " ");
        if(currentNode.left != null) {
            preOrder(currentNode.left);
        }
        if(currentNode.right != null) {
            preOrder(currentNode.right);
        }

    }

    // postOrder tree traversal
    public static void postOrder(Node root) {
        Node currentNode = root;
        if(currentNode.left != null) {
            postOrder(currentNode.left);
        }
        if(currentNode.right != null) {
            postOrder(currentNode.right);
        }
        System.out.print(currentNode.data + " ");

    }

    // inOrder tree traversal
    public static void inOrder(Node root) {
        Node currentNode = root;
        if(currentNode.left != null) {
            inOrder(currentNode.left);
        }
        System.out.print(currentNode.data + " ");
        if(currentNode.right != null) {
            inOrder(currentNode.right);
        }
    }


}
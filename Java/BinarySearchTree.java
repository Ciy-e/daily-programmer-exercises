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



import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Vector;

public class BFS {
    static Vector<Integer>[] nodes;
    private static  int node=3;
    private static int edges=2;
    public static void main(String[] args) {

        BFS();

    }

    private static void BFS() {
        takeInput();

    }
    ///i am chinmoy user
//for taking input
    private static void takeInput() {
        
        nodes = new Vector[node];
        for (int i = 0; i < edges; i++)
            nodes[i] = new Vector<>();
        int x, y;
        for (int i = 0; i < edges; i++) {
            x = new Scanner(System.in).nextInt();
            y = new Scanner(System.in).nextInt();

            nodes[x - 1].addElement(y - 1);
        }

        //Needs to be implemented

    }

}


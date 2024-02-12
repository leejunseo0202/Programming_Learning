import java.io.*;
import java.util.StringTokenizer;

class Circle{
    double x, y, r;

    public Circle(String x, String y, String r){
        this.x = Double.parseDouble(x);
        this.y = Double.parseDouble(y);
        this.r = Double.parseDouble(r);
    }
    public double CalculateDistance(double x2, double y2){
        double distance;
        return distance = Math.sqrt(Math.pow(x - x2, 2) + Math.pow(y - y2, 2));
    }
    public int CircleRelationship(Circle circle2, double distance){
        double sum = r + circle2.r;
        double sub = Math.abs(r - circle2.r);

        if(distance < sub)          return 0;
        else if(distance == sub)    return 1;
        else if(distance > sub && distance < sum)   return 2;
        else if(distance == sum)    return 1;
        else if(distance > sum)     return 0;
        else return 100;
    }

    @Override
    public boolean equals(Object obj) {
        Circle circle = (Circle)obj;
        if(x == circle.x && y == circle.y)  return true;
        else                                return false;
    }
}

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int i = Integer.parseInt(br.readLine());
        for(;i>0;i--) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            Circle circle1 = new Circle(st.nextToken(), st.nextToken(), st.nextToken());
            Circle circle2 = new Circle(st.nextToken(), st.nextToken(), st.nextToken());

            if(circle1.equals(circle2)) {
                if (circle1.r == circle2.r) bw.write("-1\n");
                else bw.write("0\n");
                continue;
            }

            double distance = circle1.CalculateDistance(circle2.x, circle2.y);
            int n = circle1.CircleRelationship(circle2, distance);

            bw.write(String.valueOf(n) + "\n");
        }

        br.close();
        bw.close();
    }
}
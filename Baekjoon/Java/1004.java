import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static int check_Including_Point(int[]point, int[]circle){
        double distance_start_point = Math.sqrt(Math.pow(point[0] - circle[0], 2) + Math.pow(point[1] - circle[1], 2));
        double distance_end_point = Math.sqrt(Math.pow(point[2] - circle[0], 2) + Math.pow(point[3] - circle[1], 2));

        int including_start_point = 0;
        int including_end_point = 0;
        if(distance_start_point < circle[2])    including_start_point = 1;
        if(distance_end_point < circle[2])      including_end_point = 1;

        if(including_start_point == 1 && including_end_point == 1)  return 0;
        else if(including_start_point == 0 && including_end_point == 0) return 0;
        else                                                            return 1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int i = Integer.parseInt(br.readLine());
        for(;i>0;i--){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            //[0]=start_x, [1]=start_y, [2]=end_x, [3]=end_y
            int point[] = new int[4];
            for(int j=0;j<4;j++)    point[j] = Integer.parseInt(st.nextToken());

            int count = 0;
            int j = Integer.parseInt(br.readLine());
            for(;j>0;j--) {

                //[0]=circle_x, [1]=circle_y, [2]=circle_r
                int circle[] = new int[3];
                st = new StringTokenizer(br.readLine(), " ");
                for(int k=0;k<3;k++)    circle[k] = Integer.parseInt(st.nextToken());

                int num = check_Including_Point(point, circle);
                count += num;
            }
            bw.write(String.valueOf(count) + "\n");
        }
        bw.close();
    }
}
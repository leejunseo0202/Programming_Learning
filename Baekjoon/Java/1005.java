import java.io.*;
import java.util.StringTokenizer;


public class Main {
    //건설해야하는 건물, 건물 수, 건물 관계, 건설 시간
    public static int minimun_Time(int building, int num, int[][] relation, int[] time){
        int max = 0;
        for(int i = 0;i<num;i++){
            if(relation[i][building] == -1)
                relation[i][building] = minimun_Time(i, num, relation, time);

            if(relation[i][building] > max)
                max = relation[i][building];
        }
        return max + time[building];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int test_time = Integer.parseInt(br.readLine());
        for(int i = test_time;i>0;i--){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int building_num = Integer.parseInt(st.nextToken());
            int building_rule = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine(), " ");
            int building_time[] = new int[building_num];
            for(int j = 0;j<building_num;j++)
                building_time[j] = Integer.parseInt(st.nextToken());

            int building_relation[][] = new int[building_num][building_num];
            for(int j = 0;j<building_rule;j++){
                st = new StringTokenizer(br.readLine(), " ");
                int building1 = Integer.parseInt(st.nextToken()) - 1;
                int building2 = Integer.parseInt(st.nextToken()) - 1;

                building_relation[building1][building2] = -1;
            }

            int building_main = Integer.parseInt(br.readLine()) - 1;
            int time = 0;

            time = minimun_Time(building_main, building_num, building_relation, building_time);

            bw.write(String.valueOf(time)+"\n");
        }

        bw.close();
    }
}
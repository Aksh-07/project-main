package py4j;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
public class AppClass

{
    public int send_python_obj_to_java( app_1 e)
    {
       
        return 0;
    }
    public String fill_data_for_speech_request() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Insufficient input\nEnter input again : ");  
            String str = br.readLine();
            return str;        
    }
    public String enterinput() throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Enter input :");  
            String str = br.readLine();
            return str;        
    }
    

    public int update_new_words_cloud(ArrayList<Object> b,app_1 e)
    { 
        System.out.println(b);
        return 0;
    }
    public int process_user_actions(ArrayList<Object> c)
    {
        return 0;
    }
 
     public static void main(String[] args) {
        AppClass y=new AppClass();
        GatewayServer gatewayServer = new GatewayServer(y);
        gatewayServer.start();
        
        System.out.println("Gateway Server Started");
        // gatewayServer.shutdown();

    }



}
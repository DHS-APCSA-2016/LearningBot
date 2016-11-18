import com.mashape.unirest.http.*;
import com.mashape.unirest.http.exceptions.UnirestException;
import java.util.Scanner;
import org.json.JSONObject;
/**
 * Write a description of class Bot here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Bot
{
    public static void main() throws UnirestException{
        System.out.println("Welcome to a new kind of AI (not really). \nJust talk to me and I'll communicate with my Python back end to talk to you!\n\nHave Fun!");
        while(true){
            System.out.print("> ");
            Scanner sc = new Scanner(System.in);
            String input = sc.nextLine();
            if(input.equals(":q")){
                System.out.println("Bye!!");
                break;
            } else {
 
                HttpResponse<String> jsonResponse = Unirest.post("http://localhost:5000/")
                  .header("Content-Type", "application/json; charset=UTF-8")
                  .header("Accept", "application/json")
                  //.field("input", input)
                  .body("{\"input\": \"" + input + "\"}")
                  .asString();
                JSONObject json = new JSONObject(jsonResponse.getBody());
                String msg = json.getString("text");
                System.out.println(msg);

            }
        }
    }
}

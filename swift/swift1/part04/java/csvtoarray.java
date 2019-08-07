import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class csvtoarray {

    public static void main(String[] args) {

        String csvFile = "stu.txt";
        String line = "";
        String cvsSplitBy = ",";
	String[] array = new String[25];

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
	    int i = 0;

            while ((line = br.readLine()) != null) {

                // use comma as separator
                //String[] stu = line.split(cvsSplitBy);
		
		array[i] = line;
		System.out.println(array[i]);
		i++;

                

            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}


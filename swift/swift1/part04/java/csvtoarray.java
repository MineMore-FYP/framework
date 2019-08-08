import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
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

		//Write each row to new txt/csv. AKA one txt for one record
		FileWriter csvWriter = new FileWriter("newline"+i+".txt");
		
		array[i] = line;
		System.out.println(array[i]);
		csvWriter.append(array[i]);
		csvWriter.flush();
		csvWriter.close();
		i++;

                

            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}


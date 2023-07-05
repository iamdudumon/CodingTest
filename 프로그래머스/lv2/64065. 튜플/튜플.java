import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

class Solution {
    public ArrayList<Integer> solution(String s) {
        //StringBuilder sb = new StringBuilder();
    	ArrayList<Integer> answer = new ArrayList<Integer>();
        String tuple = new String(s);
        
        String list = tuple.replace("{", "").replace("}", "");
        String[] slice = list.split(",");
        Map<String, Integer> map = new HashMap<String, Integer>();
        
        for(int i = 0; i < slice.length; i++) {
        	String key = slice[i];
        	if(map.containsKey(key)) {
        		//System.out.println(list.charAt(i));
        		map.replace(key, map.get(key) + 1);
        	}
        	else
        		map.put(key, 1);
        }
        
        List<Entry<String, Integer>> list_entries = new ArrayList<Entry<String, Integer>>(map.entrySet());

        
        Collections.sort(list_entries, new Comparator<Entry<String, Integer>>() {
			// compare로 값을 비교
			public int compare(Entry<String, Integer> obj1, Entry<String, Integer> obj2) {
				// 오름 차순 정렬
				return obj2.getValue().compareTo(obj1.getValue());
			}
		});
		
//    	sb.append("[");
//    	for (Entry<String, Integer> entry : list_entries){
//			sb.append(entry.getKey());
//			sb.append(",");
//		}
//    	sb.replace(sb.length() - 1, sb.length(), "");
//    	sb.append("]");
    	
        for (Entry<String, Integer> entry : list_entries){
			answer.add(Integer.valueOf(entry.getKey()));
		}
        
    	//String answer = sb.toString();
        return answer;
    }
}

import java.util.*;

public class Test {
    public static Object find_Top_Index(int[] lst) {
        ArrayList<Integer> result = new ArrayList<>();
        for(int i=1;i<lst.length;i++){
            if (lst[i]>lst[i-1] && lst[i]>lst[i+1]){
                result.add(i);
            }
        }
    }

    // 示例测试用例
    public static void main(String[] args) {
        int[] lst = {1, 3, 2, 5, 4, 6, 3};
        Object result = find_Top_Index(lst);
        System.out.println("峰值索引为：" + result);
    }
}

package site.orangefield.mongodbtest.domain;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
@Document(collection = "navers") // yml에는 DB 이름, 여기는 DB 안의 collection
public class News {
    @Id
    private String _id;
    private String title;
    private String company;
    private String createdAt;
}

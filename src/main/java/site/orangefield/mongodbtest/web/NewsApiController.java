package site.orangefield.mongodbtest.web;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import lombok.RequiredArgsConstructor;

import site.orangefield.mongodbtest.domain.NewsRepository;

@RequiredArgsConstructor
@RestController
public class NewsApiController {

    private final NewsRepository newsRepository;

    @GetMapping("/navers")
    public ResponseEntity<?> findAll() {
        return new ResponseEntity<>(newsRepository.findAll(), HttpStatus.OK);
    }

}

package com.example.demo.service;

import com.example.demo.dto.Movie;
import com.example.demo.repository.MovieRepository;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.net.URI; // URL 대신 URI를 먼저 사용
import java.util.List;

@Service
@RequiredArgsConstructor
public class MovieService {

    private final MovieRepository movieRepository;
    private final ObjectMapper objectMapper;

    @Transactional
    public void loadJson() throws Exception {
        // 1. GitHub Raw URL (URI.create를 사용하여 최신 방식 적용)
        String githubRawUrl = "https://raw.githubusercontent.com/fsclass-n/fs/main/demo/data/movies.json";
        
        // 2. URI를 거쳐 URL로 변환 (취소선 해결)
        var url = URI.create(githubRawUrl).toURL();
        
        // 3. JSON 데이터를 리스트로 변환
        // InputStream을 열어서 읽는 것이 더 안전합니다.
        List<Movie> movies;
        try (var inputStream = url.openStream()) {
            movies = objectMapper.readValue(inputStream, new TypeReference<List<Movie>>() {});
        }

        // 4. 기존 데이터 삭제 후 새로 적재
        movieRepository.deleteAll();
        movieRepository.saveAll(movies);
        
        System.out.println("🚀 GitHub 최신 데이터를 성공적으로 TiDB에 적재했습니다.");
    }

    public List<Movie> getAll() {
        return movieRepository.findAll();
    }
}
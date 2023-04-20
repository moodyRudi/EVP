package com.example.demo;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;

import java.sql.Timestamp;
import java.util.UUID;

@Component
@RequiredArgsConstructor
public class Jdbc {

    @Autowired
    JdbcTemplate jdbcTemplate;

    public void insertIntoDatabase(boolean signal) {
        UUID uuid = UUID.randomUUID();
        jdbcTemplate.update("""
                INSERT INTO Signal (id,signal, timestamp) VALUES(?,?,?)""",
                uuid, signal, new Timestamp(System.currentTimeMillis()));
    }
    public boolean getFromDatabase() {
        var query = "SELECT * FROM Signal ORDER BY timestamp DESC LIMIT 1";
        Signal signal = jdbcTemplate.queryForObject(query, new ResultMapper());
        return signal.isSignal();
    }
}

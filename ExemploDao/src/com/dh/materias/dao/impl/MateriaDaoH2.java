package com.dh.materias.dao.impl;

import com.dh.materias.dao.ConfiguracaoJDBC;
import com.dh.materias.dao.IDao;
import com.dh.materias.model.Materia;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class MateriaDaoH2 implements IDao<Materia> {
    private ConfiguracaoJDBC configuracaoJDBC;

    public MateriaDaoH2(ConfiguracaoJDBC configuracaoJDBC){
        this.configuracaoJDBC = configuracaoJDBC;
    }

    @Override
    public Materia salvar(Materia materia) {
        Connection connection = configuracaoJDBC.conectarComBancoDeDados();
        Statement statement = null;
        String query = String.format("INSERT INTO materias(nome) VALUES('%s')", materia.getNome());
        try {
            statement = connection.createStatement();
            statement.executeUpdate(query, statement.RETURN_GENERATED_KEYS);
            ResultSet keys = statement.getGeneratedKeys();
            if (keys.next())
                materia.setId(keys.getInt(1));
            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return materia;
    }

    @Override
    public List<Materia> buscarTodos() {
        Connection connection = configuracaoJDBC.conectarComBancoDeDados();
        Statement statement = null;
        String query = String.format("SELECT * FROM materias");
        List<Materia> materias = new ArrayList<>();
        try {
            statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(query);
            while (resultSet.next()) {
                materias.add(new Materia(resultSet.getInt("id"), resultSet.getString("nome")));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return materias;
    }
}

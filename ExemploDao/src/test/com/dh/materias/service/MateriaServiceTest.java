package test.com.dh.materias.service;

import com.dh.materias.dao.ConfiguracaoJDBC;
import com.dh.materias.dao.impl.MateriaDaoH2;
import com.dh.materias.model.Materia;
import com.dh.materias.serv.MateriaService;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class MateriaServiceTest {
    private MateriaService materiaService = new MateriaService(new MateriaDaoH2(new ConfiguracaoJDBC()));

    @Test
    public void salvarMateriaTeste(){
        Materia materia = new Materia("BackEnd");

        Materia materiaRegistrada = materiaService.salvar(materia);

        assertTrue(materiaRegistrada.getId() != null);
    }

    @Test
    public void buscarTodosTest(){
        Materia materia = new Materia("Backend");
        materiaService.salvar(materia);

        List<Materia> materias = materiaService.buscarTodos();

        assertEquals(1, materias.size());
    }
}
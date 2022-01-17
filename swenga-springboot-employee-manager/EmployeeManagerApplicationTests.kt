package at.fhj.ima.employee.employeemanager

import at.fhj.ima.employee.employeemanager.repository.DepartmentRepository
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Assertions
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;

@SpringBootTest(
	classes = [EmployeeManagerApplication::class],
	webEnvironment = WebEnvironment.RANDOM_PORT
)
internal class EmployeeManagerApplicationTests {

	@Test
	fun sampleUnitTest() {
		Assertions.assertEquals(1,1)

	}

	@Autowired
	lateinit var departmentRepository: DepartmentRepository

	@Test
	fun sampleIntegrationTest() {
		Assertions.assertEquals(departmentRepository.findAll().size, 3)
	}

}

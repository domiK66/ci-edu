package at.fhj.ima.swenga_guestbook.classes

import at.fhj.ima.swenga_guestbook.models.GuestBookEntry
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test
import java.time.LocalDateTime
import java.time.Month

internal class GuestBookManagerTest {
    private val gbm = GuestBookManager()

    @Test
    fun testAdd() {
        gbm.add(GuestBookEntry("Dominik","Dominik","Hallo", LocalDateTime.of(2021, Month.NOVEMBER, 29, 12, 21,)))
        Assertions.assertEquals(gbm.entries[0], GuestBookEntry("Dominik","Dominik","Hallo", LocalDateTime.of(2021, Month.NOVEMBER, 29, 12, 21,)))
    }

    @Test
    fun testIsEmpty() {
        Assertions.assertEquals(gbm.isEmpty, true)
        gbm.add(GuestBookEntry("Dominik", "Dominik", "Hallo", LocalDateTime.of(2021, Month.NOVEMBER, 29, 12, 21,)))
        Assertions.assertEquals(gbm.isEmpty, false)
    }
}
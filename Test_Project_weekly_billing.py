import unittest
import Project_weekly_billing

class TestWeeklyBilling(unittest.TestCase):

    def test_project(self):
        self.assertEqual(Project_weekly_billing.Project("19210_3M_CSS").project_name,"19210_3M_CSS")    
        self.assertEqual(Project_weekly_billing.Project("19210_3M_CSS").total_hours_spent,167.95)
        #self.assertEqual(Project_weekly_billing.Project("19210_3M_CSS").total_hours_spent,167.95)

    def test_projec(self):
        self.assertEqual(Project_weekly_billing.Project("19210_3M_CSS").project_name,"19210_3M_CSS")    
        self.assertEqual(Project_weekly_billing.Project("19210_3M_CSS").total_hours_spent,167.95)

    def test_proje(self):
        self.assertEqual(Project_weekly_billing.Project("19210_3M_CSS").project_name,"19210_3M_CSS")    
        self.assertEqual(Project_weekly_billing.Project("19210_3M_CSS").total_hours_spent,167.95)       


if __name__ == "__main__":
    unittest.main()        
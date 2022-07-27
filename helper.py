
class Helper():

    def modify_records_view(self, records):
        final_cut = []
        if not records:
            return final_cut
        else:
            for record in records:
                data = {
                    "course_id": record[0],
                    "course_name": record[1],
                    "course_timespan": record[2],
                    "fees": record[3],
                    "description": record[4]
                }
                final_cut.append(data)
        return final_cut
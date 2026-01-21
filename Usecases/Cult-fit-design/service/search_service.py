from storage import CENTERS

class SearchService:

    @staticmethod
    def search(center_id=None, class_type=None):
        results = []
        # print(f" 11111 >>> {CENTERS}")

        for center in CENTERS.values():
            if center_id and center.id != center_id:
                continue

            for cls in center.class_sessions:
                if class_type and cls.class_type != class_type:
                    continue
                results.append(cls)

        return results

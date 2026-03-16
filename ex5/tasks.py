import xml.etree.ElementTree as ET

def create_student(xml_root, student_id):
    '''
    Vytvořte studenta dle loginu.
    Ujistěte se, že student neexistuje, jinak: raise Exception('student already exists')
    '''
    if xml_root.find(f"student[@student_id = '{student_id}']") is not None:
        raise Exception('student already exists')
    
    ET.SubElement(xml_root, 'student', student_id=student_id)

def remove_student(xml_root, student_id):
    '''
    Odstraňte studenta dle loginu
    '''
    student_to_remove = xml_root.find(f"student[@student_id = '{student_id}']")

    if student_to_remove is not None:
        xml_root.remove(student_to_remove)


def set_task_points(xml_root, student_id, task_id, points):
    '''
    Přepište body danému studentovi u jednoho tasku
    '''
    student = xml_root.find(f"student[@student_id = '{student_id}']")
    if student is not None:
        task = student.find(f"task[@task_id = '{task_id}']")
        if task is not None:
            task.text = points


def create_task(xml_root, student_id, task_id, points):
    '''
    Pro daného studenta vytvořte task s body.
    Ujistěte se, že task (s task_id) u studenta neexistuje, jinak: raise Exception('task already exists')
    '''

    student = xml_root.find(f"student[@student_id = '{student_id}']")

    if student is not None:
        if student.find(f"task[@task_id='{task_id}']") is not None:
            raise Exception('task already exists')
        
        new_task = ET.SubElement(student, 'task', task_id = task_id)
        new_task.text = points


def remove_task(xml_root, task_id):
    '''
    Napříč všemi studenty smažte task s daným task_id
    '''
    for student in xml_root.findall('student'):
        task_to_remove = student.find(f"task[@task_id='{task_id}']")
        
        if task_to_remove is not None:
            student.remove(task_to_remove)

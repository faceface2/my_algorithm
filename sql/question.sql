-- 1、查询" 01 "课程比" 02 "课程成绩高的学生的信息及课程分数
SELECT * FROM Student RIGHT JOIN (
SELECT t1.SId,class1,class2 
FROM
	( SELECT SId, score AS class1 FROM SC WHERE SC.CId = '01' ) AS t1,
	( SELECT SId, score AS class2 FROM SC WHERE SC.CId = '02' ) AS t2 
WHERE
	t1.SId = t2.SId AND t1.class1 > t2.class2 
	) r ON Student.SId = r.SId;
	
	--  left join
SELECT *  FROM (
SELECT t1.SId,class1, class2 
FROM
	( SELECT SId, score AS class1 FROM SC WHERE SC.CId = '01' ) AS t1,
	( SELECT SId, score AS class2 FROM SC WHERE SC.CId = '02' ) AS t2 
WHERE t1.SId = t2.SId AND t1.class1 > t2.class2 ) r
	LEFT JOIN Student ON Student.SId = r.SId;
	
-- 2、查询同时存在" 01 "课程和" 02 "课程的情况

SELECT * 
FROM
	( SELECT * FROM SC WHERE SC.CId = '01' ) AS t1,
	( SELECT * FROM SC WHERE SC.CId = '02' ) AS t2 
WHERE t1.SId = t2.SId;

-- 3、查询存在" 01 "课程但可能不存在" 02 "课程的情况(不存在时显示为null )
SELECT
	* 
FROM
	( SELECT * FROM SC WHERE SC.CId = '01' ) AS t1
	LEFT JOIN ( SELECT * FROM SC WHERE SC.CId = '02' ) AS t2 ON t1.SId = t2.SId;
	
-- 4、查询不存在" 01 "课程但存在" 02 "课程的情况

SELECT * from SC WHERE SC.SId not in (SELECT SId from SC WHERE SC.CId='01') AND SC.CId = '02';

-- 5、查询平均成绩大于等于60 分的同学的学生编号和学生姓名和平均成绩
-- 联合搜索
SELECT  Student.SId, Student.Sname,r.ss from Student,
(SELECT SC.SId,avg(score) as ss from SC GROUP BY SId HAVING AVG(score) > 60) as r
WHERE r.SId = Student.SId;
-- RIGHT JOIN 版本
SELECT  Student.SId,Student.Sname, r.ss from Student RIGHT JOIN (
SELECT SId, AVG(score) as ss from SC GROUP BY SId HAVING AVG(score) > 60
)r on Student.SId = r.SId;

-- LEFT JOIN 版本
SELECT  Student.SId,Student.Sname, r.ss from (
SELECT SId, AVG(score) as ss from SC GROUP BY SId HAVING AVG(score) > 60
)r left join Student on Student.SId = r.SId;


-- 6、查询在SC 表存在成绩的学生信息
SELECT  Student.* from Student,SC WHERE Student.SId = SC.SId;

-- 7、查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩(没成绩的显示为null )
-- 不能显示NULL的记录
SELECT  Student.SId,Student.Sname, r.cnb,r.scoresum from Student,(
SELECT SC.SId,count(SC.CId) as cnb, SUM(SC.score) as scoresum from SC GROUP BY SC.SId
)r WHERE r.SId = Student.SId;
-- 可以显示NULL
SELECT  Student.SId,Student.Sname, r.cnb,r.scoresum 
from Student LEFT JOIN 
(SELECT SC.SId, SUM(SC.score) as scoresum, count(SC.SId) as cnb 
from SC GROUP BY SC.SId)r on Student.SId=r.SId;

-- 8、查有成绩的学生信息
-- EXISTS 适合B表比A表数据大的情况
SELECT * from Student WHERE EXISTS( SELECT SC.SId FROM SC WHERE Student.SId=SC.SId);
-- in
SELECT * from Student WHERE Student.SId in (SELECT SC.SId FROM SC);

-- 9、查询「李」姓老师的数量
SELECT COUNT(*) from Teacher WHERE Tname LIKE "李%";

-- 10、查询学过「张三」老师授课的同学的信息
SELECT Student.* from Student,Teacher,Course,SC
WHERE Student.SId = SC.SId 
and SC.CId = Course.CId
and Course.TId = Teacher.TId
and Teacher.Tname="张三";

SELECT Student.* from Student 
INNER JOIN SC ON Student.SId=SC.SId 
INNER JOIN Course ON SC.CId = Course.CId
INNER JOIN Teacher ON Course.TId=Teacher.TId
WHERE Teacher.Tname="张三";

-- 11、查询没有学全所有课程的同学的信息
SELECT * FROM Student 
WHERE Student.SId not in (
SELECT SC.SId FROM SC GROUP BY SC.SId HAVING COUNT(SC.CId) = (SELECT COUNT(*) FROM Course)
)
-- 12、查询至少有一门课与学号为" 01 "的同学所学相同的同学的信息
SELECT * FROM Student
WHERE Student.SId in (
SELECT SC.SId FROM SC WHERE SC.CId IN ( SELECT SC.CId FROM SC WHERE SId="01")
);
-- 13、查询和" 01 "号的同学学习的课程完全相同的其他同学的信息
SELECT * FROM Student WHERE not EXISTS(
	SELECT * FROM SC sc1 WHERE sc1.SId='01' AND not EXISTS(
		SELECT * FROM SC sc2 WHERE sc2.SId=Student.SId AND sc1.CId=sc2.CId
	)
)
-- 14、查询没学过"张三"老师讲授的任一门课程的学生姓名
SELECT * FROM Student WHERE Student.SId not IN(
SELECT SC.SId FROM SC WHERE SC.CId in (
	SELECT Course.CId FROM Course WHERE Course.TId in (
	SELECT Teacher.TId FROM Teacher WHERE Teacher.Tname="张三")
)
)
-- / 联合查询
SELECT * FROM Student WHERE Student.SId not in (
SELECT SC.SId FROM SC, Course,Teacher 
WHERE SC.CId = Course.CId 
and Course.TId = Teacher.TId
AND Teacher.Tname="张三"
)

-- 15、查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
SELECT Student.SId, any_value(Student.Sname), AVG(sc.score) 
FROM Student, (SELECT * FROM SC WHERE SC.score < 60) as sc
WHERE Student.SId = sc.SId
GROUP BY sc.SId
HAVING COUNT(*) >= 1;

-- 16、检索" 01 "课程分数小于60，按分数降序排列的学生信息
SELECT Student.*,SC.score FROM Student,SC
WHERE Student.SId =SC.SId
AND SC.score < 60
AND SC.CId = "01"
ORDER BY SC.score DESC;

-- 17、按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩

-- 18、查询各科成绩最高分、最低分和平均分：
-- 以如下形式显示：课程ID，课程name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
-- 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
-- 要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
-- 按各科成绩进行排序，并显示排名，Score 重复时保留名次空缺
-- 15.1 按各科成绩进行排序，并显示排名，Score 重复时合并名次
-- 查询学生的总成绩，并进行排名，总分重复时保留名次空缺
-- 16.1 查询学生的总成绩，并进行排名，总分重复时不保留名次空缺
-- 统计各科成绩各分数段人数：课程编号，课程名称，[100-85]，[85-70]，[70-60]，[60-0] 及所占百分比
-- 查询各科成绩前三名的记录
-- 查询每门课程被选修的学生数
-- 查询出只选修两门课程的学生学号和姓名
-- 查询男生、女生人数
-- 查询名字中含有「风」字的学生信息
-- 查询同名同性学生名单，并统计同名人数
-- 查询1990 年出生的学生名单
-- 查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
-- 查询平均成绩大于等于85 的所有学生的学号、姓名和平均成绩
-- 查询课程名称为「数学」，且分数低于60 的学生姓名和分数
-- 查询所有学生的课程及分数情况（存在学生没成绩，没选课的情况）
-- 查询任何一门课程成绩在70 分以上的姓名、课程名称和分数
-- 查询不及格的课程
-- 查询课程编号为01 且课程成绩在80 分以上的学生的学号和姓名
-- 求每门课程的学生人数
-- 成绩不重复，查询选修「张三」老师所授课程的学生中，成绩最高的学生信息及其成绩
-- 成绩有重复的情况下，查询选修「张三」老师所授课程的学生中，成绩最高的学生信息及其成绩
-- 查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
-- 查询每门功成绩最好的前两名
-- 统计每门课程的学生选修人数（超过5 人的课程才统计）。
-- 检索至少选修两门课程的学生学号
-- 查询选修了全部课程的学生信息
-- 查询各学生的年龄，只按年份来算
-- 按照出生日期来算，当前月日< 出生年月的月日则，年龄减一
-- 查询本周过生日的学生
-- 查询下周过生日的学生
-- 查询本月过生日的学生
-- 查询下月过生日的学生